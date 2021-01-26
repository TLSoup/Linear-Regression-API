const App = (() => {
    let app = {}
    app.init = () => {
        console.log('Hello World')
        showGraph()
    }
    const showGraph = () => {
        console.log('showing graph')
    }
    return app
})()
document.addEventListener('DOMContentLoaded', () => {
    App.init()
})