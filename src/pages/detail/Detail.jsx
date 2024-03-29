import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router';

import tmdbApi from '../../api/tmdbApi';
import apiConfig from '../../api/apiConfig';

import './detail.scss';
import CastList from './CastList';
// import VideoList from './VideoList';

// import MovieList from '../../components/movie-list/MovieList';

const Detail = () => {
  const { category, id } = useParams();
  const [item, setItem] = useState(null);
  const [mtarsRating, setMtarsRating] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const getDetail = async () => {
      const response = await tmdbApi.detail(category, id, { params: {} });
      setItem(response);
      setLoading(true);
      console.log(loading);
      window.scrollTo(0, 0);
    };
    getDetail();

    const getMTARSRating = async () => {
      let query = '/api/mtarsrating?movie=' + item.title;
      const response = await fetch(query);
      const jsonData = await response.json();
      setMtarsRating(jsonData);
    };

    if (loading) {
      getMTARSRating();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [category, id, loading]);

  return (
    <>
      {item && (
        <>
          <div
            className='banner'
            style={{
              backgroundImage: `url(${apiConfig.originalImage(
                item.backdrop_path || item.poster_path
              )})`,
            }}
          ></div>
          <div className='mb-3 movie-content container'>
            <div className='movie-content__poster'>
              <div
                className='movie-content__poster__img'
                style={{
                  backgroundImage: `url(${apiConfig.originalImage(
                    item.poster_path || item.backdrop_path
                  )})`,
                }}
              ></div>
            </div>
            <div className='movie-content__info'>
              <h1 className='title'>{item.title || item.name}</h1>
              <div className='genres'>
                {item.genres &&
                  item.genres.slice(0, 5).map((genre, i) => (
                    <span key={i} className='genres__item'>
                      {genre.name}
                    </span>
                  ))}
              </div>
              <p className='overview'>{item.overview}</p>
              <h3 color={'red'}>Positive Ratings: {mtarsRating ? mtarsRating.response.pos : ''}</h3>
              <h3>Negative Ratings: {mtarsRating ? mtarsRating.response.neg : ''}</h3>
              <div className='cast'>
                <div className='section__header'>
                  <h2>Casts</h2>
                </div>
                <CastList id={item.id} />
              </div>
            </div>
          </div>
          {/* <div className='container'>
            <div className='section mb-3'>
              <VideoList id={item.id} />
            </div>
            <div className='section mb-3'>
              <div className='section__header mb-2'>
                <h2>Similar</h2>
              </div>
              <MovieList category={category} type='similar' id={item.id} />
            </div>
          </div> */}
        </>
      )}
    </>
  );
};

export default Detail;
