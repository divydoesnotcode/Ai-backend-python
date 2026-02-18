import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BackgroundBeamsDemo } from '../components/ui/backgroundBeamsDemo'
import { PlaceholdersAndVanishInputDemo } from '../components/ui/placeholderAndVanishInput'
import { StatefulButtonDemo } from '../components/ui/statefulButton'

function App() {
  const [count, setCount] = useState(0)

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
