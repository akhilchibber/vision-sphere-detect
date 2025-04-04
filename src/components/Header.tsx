
import React from 'react';
import { Aperture } from 'lucide-react';

const Header = () => {
  return (
    <header className="flex items-center space-x-3 mb-8">
      <div className="bg-accent/10 p-2 rounded-full">
        <Aperture className="w-8 h-8 text-accent" />
      </div>
      <h1 className="text-2xl font-semibold text-primary">Gravestein Vision</h1>
    </header>
  );
};

export default Header;
