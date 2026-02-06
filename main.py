from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from ollama_service import generate_vendors_llm
from vendor_repo import save_vendors_to_db, get_vendors_from_db


from database import get_db
from models import Vendor
import schemas

app = FastAPI()

@app.post("/")
async def root():
    return {"Messsage" : "Connected to ai_python PostgreSQL Database"}


# Creating Vendors

@app.post("/vendors", response_model=schemas.VendorResponse)
async def create_vendor(
    vendor: schemas.VendorCreate,
    db: AsyncSession = Depends(get_db)
):
    new_vendor = Vendor(
        id = vendor.id,
        name = vendor.name,
        location = vendor.location,
        contact = vendor.contact
    )

    db.add(new_vendor)
    await db.commit()
    await db.refresh(new_vendor)

    return new_vendor 

# Get Vendors ALL

@app.get("/vendors", response_model=schemas.VendorList)
async def get_vendors(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Vendor).order_by(Vendor.id))
    vendors = result.scalars().all()

    return {"vendors": vendors}


# Update Vendor Details

@app.put("/vendors/{vendor_id}", response_model=schemas.VendorResponse)
async def update_vendor(vendor_id: int, vendor_update: schemas.VendorCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vendor).where(Vendor.id == vendor_id))
    vendor = result.scalar_one_or_none()

    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")

    vendor.name = vendor_update.name
    vendor.location = vendor_update.location
    vendor.contact = vendor_update.contact

    await db.commit()
    await db.refresh(vendor)

    return vendor

# Delete vendor by id

@app.delete("/vendors/{vendor_id}")
async def delete_vendor(vendor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vendor).where(Vendor.id == vendor_id))
    vendor = result.scalar_one_or_none()

    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")

    await db.delete(vendor)
    await db.commit()

    return {"message": "Vendor deleted successfully"}




############## Ollama API Integration ##############



class VendorRequest(BaseModel):
    item: str
    location: str

@app.get("/generate")
def generate():
    return {"Status" : "FastAPI and Ollama Running Successfully"}

# @app.post("/generate-vendor")
# def generate_vendor(req: VendorRequest):
    
#     response = generate_vendors(req.item, req.location)
    # return {"item" : req.item, 
    #         "location" : req.location, 
    #         "vendor" : response}


# Generate and save vendors from Ollama
# @app.post("/generate-and-save-vendor")
# def generate_and_save_vendor(req: VendorRequest):
   
#    # Generate vendors from Ollama
#    result = generate_vendors(req.item, req.location)

#    vendors = result.get("vendors")

#    # Save vendors to database
#    save_vendors(req.item, vendors)

#    return {"success" : True,
#    "vendor_saved" : len(vendors),
#    "vendors" : vendors}

@app.post("/generate-vendors-flow")
def generate_vendors_flow(req: VendorRequest):

    # STEP 1: Check database first
    db_vendors = get_vendors_from_db(req.item, req.location)

    if db_vendors:
        return {
            "source": "database",
            "count": len(db_vendors),
            "vendors": db_vendors
        }

    llm_response = generate_vendors_llm(req.item, req.location)

    vendors = llm_response.get("vendors", [])

    saved_count = save_vendors_to_db(
        req.item,
        req.location,
        vendors
    )

    return {
        "source": "llm",
        "generated": len(vendors),
        "saved": saved_count,
        "vendors": vendors
    }
   
   