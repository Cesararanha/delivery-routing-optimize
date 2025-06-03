import { useEffect, useState } from "react";
import axios from "axios";
import { MapContainer, TileLayer, CircleMarker, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const cores = {
    deposito: "blue",
    hub: "orange",
    zona: "green",
};

export default function Mapa() {
    const [grafo, setGrafo] = useState(null);
    const [posicoes, setPosicoes] = useState({});

    useEffect(() => {
        axios.get("http://localhost:8000/grafo/exemplo")
            .then(res => {
                setGrafo(res.data);

                // Mapeia posições por ID
                const posicoesMap = {};
                res.data.pontos.forEach(p => {
                    posicoesMap[p.id] = [p.lat, p.lng];
                });
                setPosicoes(posicoesMap);
            })
            .catch(err => console.error("Erro ao carregar grafo:", err));
    }, []);

    if (!grafo) return <p>Carregando grafo...</p>;

    const renderMarcadores = () =>
        grafo.pontos.map(ponto => (
            <CircleMarker
                key={ponto.id}
                center={posicoes[ponto.id]}
                radius={10}
                pathOptions={{ color: cores[ponto.tipo] }}
            />
        ));

    const renderRotas = () =>
        grafo.rotas.map((rota, i) => (
            <Polyline
                key={i}
                positions={[posicoes[rota.origem], posicoes[rota.destino]]}
                pathOptions={{ color: "gray" }}
            />
        ));

    return (
        <MapContainer center={[-23.55, -46.63]} zoom={13} style={{ height: "90vh", width: "100%" }}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {renderMarcadores()}
            {renderRotas()}
        </MapContainer>
    );
}
