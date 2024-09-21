interface Medico{
    id: string;
    nombre: string;
    apellido: string;
    especialidad: string;
    telefono: string;
    email: string;
    institucion: string;
    agregado_por: string;
}

interface Especialidad{
    id: string;
    especialidad: string;
    create_at: string;
    update_at: string;
}


export { Medico, Especialidad }