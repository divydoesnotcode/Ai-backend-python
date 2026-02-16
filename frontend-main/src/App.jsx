import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BackgroundBeamsDemo } from '../components/ui/backgroundBeamsDemo'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BackgroundBeamsDemo />
    </>
  )
}

export default App
