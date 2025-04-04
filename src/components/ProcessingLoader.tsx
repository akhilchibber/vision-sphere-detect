
import React from 'react';

const ProcessingLoader = () => {
  return (
    <div className="absolute inset-0 flex flex-col items-center justify-center bg-background/80 backdrop-blur-sm z-10 rounded-lg">
      <div className="relative">
        <div className="lens-focus"></div>
        <div className="pulse-ring"></div>
      </div>
      <p className="mt-8 text-lg font-medium text-primary">Analyzing Image...</p>
      <p className="text-sm text-muted-foreground">Detecting objects with AI</p>
    </div>
  );
};

export default ProcessingLoader;
