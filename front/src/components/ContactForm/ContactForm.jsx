import { useState } from 'react';
import { useSubmitContactFormMutation } from '../../store/contactApi';
import styles from './ContactForm.module.sass';

export default function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    email: '',
  });

  // RTK Query hook provides the submit trigger function and request state
  const [submitContactForm, { isLoading, isSuccess, isError, error }] =
    useSubmitContactFormMutation();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await submitContactForm(formData).unwrap();
      setFormData({ name: '', phone: '', email: '' }); // Reset form on success
    } catch (err) {
      console.error('Failed to submit form:', err);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <div className={styles.field}>
        <label htmlFor="name">Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
      </div>

      <div className={styles.field}>
        <label htmlFor="phone">Phone Number</label>
        <input
          type="tel"
          id="phone"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          required
        />
      </div>

      <div className={styles.field}>
        <label htmlFor="email">Email</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
      </div>

      <button type="submit" disabled={isLoading} className={styles.button}>
        {isLoading ? 'Submitting...' : 'Submit'}
      </button>

      {isSuccess && <p className={styles.success}>Contact info sent successfully!</p>}
      {isError && (
        <p className={styles.error}>
          {error?.data?.detail || 'Failed to submit form.'}
        </p>
      )}
    </form>
  );
}