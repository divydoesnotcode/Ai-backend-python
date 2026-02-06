from db import get_connection
import psycopg2


def save_vendors_to_db(item_name, location, vendors):

    conn = get_connection()
    cursor = conn.cursor()

    saved_count = 0

    # Normalize item and location ONCE
    normalized_item = item_name.strip().lower()
    normalized_location = location.strip().lower()

    for vendor in vendors:

        try:
            # Normalize vendor fields
            vendor_name = vendor.get("name", "").strip().lower()
            address = vendor.get("address", "").strip()
            phone = vendor.get("phone", "").strip()
            email = vendor.get("email", "").strip()
            website = vendor.get("website", "").strip()

            # Skip empty vendor names
            if not vendor_name:
                continue

            cursor.execute("""
                INSERT INTO vendors
                (item_name, location, vendor_name, address, phone, email, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (item_name, location, vendor_name)
                DO NOTHING
            """, (
                normalized_item,
                normalized_location,
                vendor_name,
                address,
                phone,
                email,
                website
            ))

            if cursor.rowcount > 0:
                saved_count += 1

        except psycopg2.Error as e:
            print("Database error:", e)

    conn.commit()

    cursor.close()
    conn.close()

    return saved_count

def get_vendors_from_db(item_name, location):

    conn = get_connection()
    cursor = conn.cursor()

    normalized_item = item_name.strip().lower()
    normalized_location = location.strip().lower()

    cursor.execute("""
        SELECT vendor_name, address, phone, email, website
        FROM vendors
        WHERE item_name = %s
        AND location = %s
    """, (normalized_item, normalized_location))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    vendors = []

    for row in rows:
        vendors.append({
            "name": row[0],
            "address": row[1],
            "phone": row[2],
            "email": row[3],
            "website": row[4]
        })

    return vendors