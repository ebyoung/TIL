import React from "react";
import Notification from "./Notification";

const reservedNotifications = [
    {
        id: 1,
        message: '안녕하세요.',
    },
    {
        id: 2,
        message: '식사 시간입니다.',
    },
    {
        id: 3,
        message: '미팅이 시작됩니다.',
    },
];

let timer;

class NotificationList extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            notifications: [],
        };
    }

    componentDidMount() {
        const { notifications, } = this.state;
        timer = setInterval(() => {
            if (notifications.length < reservedNotifications.length) {
                const index = notifications.length;
                notifications.push(reservedNotifications[index]);
                this.setState({
                    notifications,
                });
            } else {
                clearInterval(timer)
            }
        }, 1000);
    }


    render() {
        return (
            <div>
                {this.state.notifications.map((notification) => {
                    return <Notification message={notification.message} key={notification.id} id={notification.id} />;
                })}
            </div>
        );
    }
}

export default NotificationList;