const apiConfig = {
  baseUrl: 'https://api.themoviedb.org/3/',
  apiKey: '8270596cd22c18c4e5247762a9a2521d',
  originalImage: (imgPath) => `https://image.tmdb.org/t/p/original/${imgPath}`,
  w500Image: (imgPath) => `https://image.tmdb.org/t/p/w500/${imgPath}`,
};

export default apiConfig;
