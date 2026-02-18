import './App.css'
import { BackgroundBeamsDemo } from '../components/ui/backgroundBeamsDemo'
import { PlaceholdersAndVanishInputDemo } from '../components/ui/placeholderAndVanishInput'
import { StatefulButtonDemo } from '../components/ui/statefulButton'
import { SidebarLayout } from '../components/ui/sidebar-layout'

function App() {
  return (
    <SidebarLayout>
      <BackgroundBeamsDemo>
        <PlaceholdersAndVanishInputDemo />
        <StatefulButtonDemo />
      </BackgroundBeamsDemo>
    </SidebarLayout>
  )
}

export default App
