import React, { useState } from 'react';
import { Link, useNavigate  } from 'react-router-dom';

const About = () => {
  const [value, setValue] = useState('');
  const navigate = useNavigate();

  const moveToProfile = (event) => {
    event.preventDefault();
    navigate(`/profile/${value}`)
  };

  const onChange = (event) => {
    setValue(event.target.value)
  }

  return (
    <div>
      <h1>소개</h1>
      <p>리액트 라우터를 사용해 보는 프로젝트입니다.</p>
      <form onSubmit={moveToProfile}>
        <label>
          <input
            value={value}
            onChange={onChange}
          />
          <button type='submit'>이동</button>
        </label>
      </form>
      <Link to="../">뒤로</Link>
    </div>
  );
};

export default About;