export const load = async ({ fetch }) => {
    const flockHook = await fetch('local.darkcloud.ca:3337/flocks')
    const flockData = await flockHook.json()
    const flock = flockData.flock_size
    
    return {
        flock: flock
    }
}