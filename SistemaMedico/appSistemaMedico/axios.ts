import axios from "axios";

const axiosInstance = axios.create({
    baseURL: "https://backend-medics.onrender.com/api",
});

const getEspecialidades = async () => {
    const { data } = await axiosInstance.get("/especialidades");
    
    return data;
};

export { getEspecialidades };