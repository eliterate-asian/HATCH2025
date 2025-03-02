
export const load = async ({ fetch }) => {
    const flockHook = await fetch('http://local.darkcloud.ca:3337/flocks', {
            mode: 'no-cors',
            method: "post",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"genus": "x", "species": "y", "gender": "probably", "flock_size": "9000", "flock_density":"0.1"})
        })
        .then(res => res.json())
        .then(res => {
            console.log(res);
        })
}