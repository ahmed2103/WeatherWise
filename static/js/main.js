const
    API_PORT = '8000',
    API_URL = `${document.location.protocol}//${document.location.hostname}:${API_PORT}`;

const app = Vue.createApp({
    data() {
        return {
            inputCity: "",
            selectedWeatherType: "weather",
            selectedUnit: 'C',
        };
    },
    methods: {
        gotoAboutUsPage() {
            window.open(API_URL + '/about/');
        }
    },
    computed: {
        current() {
            return {
                hour: "6:00 PM",
                temp: 30,
                condition: "Clear sky",
                city: "Giza",
                country: "EG",
                date: "Mon 15 Oct 2024",
                humidity: 25,
                wind: {
                    speed: 26,
                    direction: 255,
                },
                icon: '01d'
            };
        }
    },
    watch: {
        inputCity() {

        }
    }
});
app.mount('#app');
