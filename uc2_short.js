async function get_data(url) {
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(res.status);
        const data = await res.json();
        return data.filter(d => d.act);
    } catch (err) {
        console.error(err);
        return [];
    }
}
