// const API_PORT = "8000",
//   API_URL = `${document.location.protocol}//${document.location.hostname}:${API_PORT}`,
//   IP_API = `http://for-us.tech`;
const API_URL = document.location.origin;

// response.dt + 000 ++ res.timezone

const elInputCity = document.getElementById("inp-city");

const app = Vue.createApp({
  data() {
    // fetch("https://example.com?");
    /* 
    window.initialInfo = {
        city: "{{city}}",
        country: "{{country}}",
        temp: {{temp}},
        description: "{{description}}"
      };
    */
    window.initialInfo.time = moment();
    return {
      // inputCity: (await fetch("http://for-us.tech")).json().city,
      msg: "Please select a City",
      inputCity: "",
      selectedWeatherType: "weather",
      selectedUnit: initialInfo.fav_unit || "C",
      infoReady: true,
      // dailyForecast: [],
      // weeklyForecast: [],
      current: {
        timezone: initialInfo.timezone,
        time: initialInfo.time.format("h:mm A"),
        temp: initialInfo.temp,
        temp_min: initialInfo.temp_min,
        temp_max: initialInfo.temp_max,
        condition: initialInfo.description,
        city: initialInfo.city,
        country: initialInfo.country,
        date: initialInfo.time.format("ddd D MMM YYYY"),
        humidity: initialInfo.humidity,
        wind: {
          speed: initialInfo.wind.speed,
          deg: initialInfo.wind.deg,
        },
        icon: initialInfo.icon,
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
        timezone: timezone,
        time: time.format("h:mm A"),
        temp: res.main.temp,
        temp_min: res.main.temp_min,
        temp_max: res.main.temp_max,
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
      this.fetchForecast();
      this.infoReady = true;
    },
    async fetchForecast() {
      if (
        this.current.city &&
        !this.dailyForecast.length &&
        !this.weeklyForecast.length
      ) {
        /* fetch forecast */
        var timezone = this.current.timezone;
        // daily
        res = await fetch(
          `${API_URL}/api/v1/forecast?` +
            new URLSearchParams({
              city: this.current.city,
            })
        );
        res = await res.json();
        var today = moment(res.list[0].dt * 1000 + timezone).format("ddd");
        this.dailyForecast.length = 0;
        res.list.every((i, idx) => {
          if (moment(i.dt * 1000 + timezone).format("ddd") === today) {
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
            return true;
          } else {
            res.list.slice(idx);
            return false;
          }
        });
        // weekly
        // res = await fetch(
        //   `${API_URL}/api/v1/forecast?` +
        //     new URLSearchParams({
        //       city: this.current.city,
        //       time_type: "weekly",
        //     })
        // );
        // res = await res.json();
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
      }
    },
    convertUnit(temp) {
      if (this.selectedUnit === "F") temp = ((temp * 9) / 5 + 32).toFixed(2);
      return Math.round(temp); // round the result to intiger value
    },
    setSelectedUnit(unit) {
      if (this.selectedUnit === unit) return;
      fetch(`${API_URL}/api/v1/prefered_units?units=${unit}`, {
        method: "PUT",
        headers: {
          accept: "application/json",
        },
      });
      this.selectedUnit = unit;
    },
  },
  computed: {},
  watch: {
    inputCity() {},
  },
});
app.mount("#app");
