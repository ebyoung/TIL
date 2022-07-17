import { useParams } from 'react-router-dom';

const Article = () => {
  const { id } = useParams();
  return (
    <div>
      {
        (0 <= id && id < 10) ?
        (<h2>게시글 {id}</h2>) :
        (<p>존재하지 않는 게시글입니다.</p>)
      }
    </div>
  );
};

export default Article;