import './App.css'
import { BackgroundBeamsDemo } from '../components/ui/backgroundBeamsDemo'
import { PlaceholdersAndVanishInputDemo } from '../components/ui/placeholderAndVanishInput'
import { StatefulButtonDemo } from '../components/ui/statefulButton'

function App() {
  return (
    <>
      <BackgroundBeamsDemo>
        <PlaceholdersAndVanishInputDemo />
        <StatefulButtonDemo />
      </BackgroundBeamsDemo>
    </>
  )
}

export default App
