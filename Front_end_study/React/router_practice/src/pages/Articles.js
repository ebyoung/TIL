import { NavLink, Outlet } from 'react-router-dom';
import _ from 'lodash'

const ArticleItem = ({id}) => {
  const activeStyle = {
    color: 'green',
    fontSize: 21,
  };

  return (
    <li>
      <NavLink
        to={`/articles/${id}`}
        style={({ isActive }) => (isActive ? activeStyle : undefined)}
      >
        게시글 {id}
      </NavLink>
    </li>
  )
}

const Articles = () => {
  const articleIds = _.range(10);

  return (
    <div>
      <Outlet />
      <ul>
        {
          articleIds.map((articleId, index) => {
            return <ArticleItem id={articleId} key={index} />
          })
        }
      </ul>
    </div>
  );
};

export default Articles;