const API_PORT = "8000",
  API_URL = `${document.location.protocol}//${document.location.hostname}:${API_PORT}`,
  IP_API = `http://for-us.tech`;

// response.dt + 000 ++ res.timezone

const elInputCity = document.getElementById("inp-city");

const app = Vue.createApp({
  data() {
    // fetch("https://example.com?");

    return {
      // inputCity: (await fetch("http://for-us.tech")).json().city,
      msg: "Please select a City",
      inputCity: "",
      selectedWeatherType: "weather",
      selectedUnit: "C",
      infoReady: false,
      // dailyForecast: [],
      // weeklyForecast: [],
      current: {
        time: "6:00 PM",
        temp: 30,
        condition: "Clear sky",
        city: "Giza",
        country: "EG",
        date: "Mon 15 Oct 2024",
        humidity: 25,
        wind: {
          speed: 26,
          deg: 255,
        },
        icon: "01d",
      },
      weeklyForecast: [],
      dailyForecast: [],
    };
  },
  methods: {
    gotoAboutUsPage() {
      window.open(API_URL + "/about/");
    },
    async fetchCityInfo() {
      if (!this.inputCity) {
        alert("Please select a City");
        return;
      }
      this.infoReady = false;
      this.msg = "Please wait...";
      /* fetch weather */
      var res = await fetch(
        `${API_URL}/api/v1/weather?` +
          new URLSearchParams({
            city: this.inputCity,
          })
      );
      res = await res.json();
      if (res.cod === "404") {
        alert(`${this.inputCity}: is not a valid City`);
        this.msg = "Please select a City";
        return;
      }
      var timezone = res.timezone;
      var time = moment(res.dt * 1000 + timezone);
      this.current = {
        time: time.format("h:mm A"),
        temp: res.main.temp,
        condition: res.weather[0].description,
        city: res.name,
        country: res.sys.country,
        date: time.format("ddd D MMM YYYY"),
        humidity: res.main.humidity,
        wind: {
          speed: res.wind.speed,
          deg: res.wind.deg,
        },
        icon: res.weather[0].icon,
      };
      /* fetch forecast */
      // daily
      res = await fetch(
        `${API_URL}/api/v1/forecast?` +
          new URLSearchParams({
            city: this.inputCity,
            time_type: "daily",
          })
      );
      res = await res.json();
      this.dailyForecast.length = 0;
      for (let i of res.list) {
        this.dailyForecast.push({
          time: moment(i.dt * 1000 + timezone).format("h:mm A"),
          temp: i.main.temp,
          condition: i.weather[0].description,
          humidity: i.main.humidity,
          wind: {
            speed: i.wind.speed,
            deg: i.wind.deg,
          },
          icon: i.weather[0].icon,
        });
      }
      // weekly
      res = await fetch(
        `${API_URL}/api/v1/forecast?` +
          new URLSearchParams({
            city: this.inputCity,
            time_type: "daily",
          })
      );
      res = await res.json();
      this.weeklyForecast.length = 0;
      var last_day = undefined,
        day;
      for (let i of res.list) {
        day = moment(i.dt * 1000 + timezone).format("ddd");
        if (day === last_day) continue;
        last_day = day;
        this.weeklyForecast.push({
          time: day,
          temp: i.main.temp,
          condition: i.weather[0].description,
          humidity: i.main.humidity,
          wind: {
            speed: i.wind.speed,
            deg: i.wind.deg,
          },
          icon: i.weather[0].icon,
        });
      }
      this.infoReady = true;
    },
    convertUnit(temp) {
      if (this.selectedUnit === "F") return ((temp * 9) / 5 + 32).toFixed(2);
      else return temp;
    },
  },
  computed: {},
  watch: {
    inputCity() {},
  },
});
app.mount("#app");
