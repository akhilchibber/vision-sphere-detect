
import React from 'react';
import { Download } from 'lucide-react';
import { Button } from '@/components/ui/button';

interface Detection {
  label: string;
  confidence: number;
  box: {
    x: number;
    y: number;
    width: number;
    height: number;
  };
}

interface ResultDisplayProps {
  imageUrl: string;
  detections: Detection[];
  onAnalyzeAnother: () => void;
}

const ResultDisplay = ({ imageUrl, detections, onAnalyzeAnother }: ResultDisplayProps) => {
  // Group detections by label
  const groupedDetections = detections.reduce((acc, detection) => {
    const { label } = detection;
    if (!acc[label]) {
      acc[label] = [];
    }
    acc[label].push(detection);
    return acc;
  }, {} as Record<string, Detection[]>);
  
  // Count total objects
  const totalObjects = detections.length;
  
  // Mock function for download result
  const handleDownload = () => {
    const link = document.createElement('a');
    link.href = imageUrl;
    link.download = 'detected-objects.jpg';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="flex flex-col lg:flex-row gap-6">
      <div className="lg:w-2/3 relative">
        <div className="bg-white p-2 rounded-lg shadow-sm">
          <img 
            src={imageUrl} 
            alt="Detected Objects" 
            className="w-full h-auto rounded"
          />
        </div>
        <div className="absolute bottom-4 right-4">
          <Button 
            variant="secondary" 
            size="sm"
            className="flex items-center gap-2"
            onClick={handleDownload}
          >
            <Download className="w-4 h-4" />
            Save Result
          </Button>
        </div>
      </div>
      
      <div className="lg:w-1/3">
        <div className="bg-card rounded-lg shadow-sm p-6">
          <h3 className="text-lg font-medium mb-4">Detection Results</h3>
          
          <div className="mb-4">
            <div className="text-sm font-medium text-muted-foreground mb-2">
              Total Objects Detected: <span className="text-primary">{totalObjects}</span>
            </div>
          </div>
          
          <div className="space-y-4 max-h-80 overflow-y-auto pr-2">
            {Object.entries(groupedDetections).map(([label, items]) => (
              <div key={label} className="pb-3 border-b last:border-0">
                <div className="flex justify-between items-center mb-2">
                  <h4 className="font-medium">{label}</h4>
                  <span className="text-xs bg-secondary px-2 py-1 rounded-full">
                    {items.length}
                  </span>
                </div>
                <div className="space-y-2">
                  {items.map((detection, idx) => (
                    <div key={idx} className="flex justify-between text-sm">
                      <span className="text-muted-foreground">Instance {idx + 1}</span>
                      <span className="font-medium">
                        {(detection.confidence * 100).toFixed(1)}% confidence
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
          
          <Button 
            className="w-full mt-6 bg-accent hover:bg-accent/80"
            onClick={onAnalyzeAnother}
          >
            Analyze Another Image
          </Button>
        </div>
      </div>
    </div>
  );
};

export default ResultDisplay;
