import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      <h1>홈</h1>
      <p>홈 페이지 입니다.</p>
      <Link to="/about">소개</Link><br/>
      <Link to="/articles">글 목록</Link>
    </div>
  );
}

export default Home;
