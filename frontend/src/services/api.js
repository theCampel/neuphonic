export const generateText = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const data = await response.json();
    return data.text;
  } catch (error) {
    console.error('Error generating text:', error);
    throw error;
  }
}; 