function TaskList({ tasks }) {
  return (
    <ul>
      {tasks.map((task, index) => (
        <li key={index}>{`${task.name}, Priority: ${task.priority}, Time: ${task.time} hours`}</li>
      ))}
    </ul>
  );
}
