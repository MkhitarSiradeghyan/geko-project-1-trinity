import React from 'react';
import { useGetAboutInfoQuery } from '../../store/api/aboutApi';

const About = () => {
  const { data: aboutData, isLoading, isError } = useGetAboutInfoQuery();

  if (isLoading) return <div>Բեռնվում է...</div>;
  if (isError || !aboutData) return <div>Տվյալները ստանալիս սխալ է տեղի ունեցել:</div>;

  return (
    <section className="about-section">
      <div className="container">
        <h2>{aboutData.title}</h2>
        <p>{aboutData.description}</p>
      </div>
    </section>
  );
};

export default About;