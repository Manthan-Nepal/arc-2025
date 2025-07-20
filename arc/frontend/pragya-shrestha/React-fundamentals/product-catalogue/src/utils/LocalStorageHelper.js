export const getLocal = (key, defaultValue = null) => {
  try {
    const saved = localStorage.getItem(key);
    return saved ? JSON.parse(saved) : defaultValue;
  } catch (e) {
    console.error("Error reading localStorage:", e);
    return defaultValue;
  }
};

export const setLocal = (key, value) => {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (e) {
    console.error("Error writing to localStorage:", e);
  }
};
