
import { useState } from 'react';
import { useToast } from '@/hooks/use-toast';
import Header from '@/components/Header';
import UploadZone from '@/components/UploadZone';
import ProcessingLoader from '@/components/ProcessingLoader';
import ResultDisplay from '@/components/ResultDisplay';
import { Button } from '@/components/ui/button';

// Mock API - In a real application, this would be replaced with actual API calls
const mockDetectObjects = async (file: File): Promise<{
  imageUrl: string;
  detections: { 
    label: string;
    confidence: number;
    box: { x: number; y: number; width: number; height: number; }
  }[];
}> => {
  // Simulate API delay
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // Return mock data
  return {
    imageUrl: URL.createObjectURL(file),
    detections: [
      { 
        label: 'Person',
        confidence: 0.92,
        box: { x: 50, y: 50, width: 200, height: 350 }
      },
      { 
        label: 'Dog',
        confidence: 0.85,
        box: { x: 300, y: 200, width: 150, height: 100 }
      },
      { 
        label: 'Car',
        confidence: 0.95,
        box: { x: 450, y: 100, width: 250, height: 150 }
      }
    ]
  };
};

// Application states
enum AppState {
  INITIAL,
  IMAGE_SELECTED,
  PROCESSING,
  RESULTS,
  ERROR
}

const Index = () => {
  const [appState, setAppState] = useState<AppState>(AppState.INITIAL);
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [results, setResults] = useState<{
    imageUrl: string;
    detections: any[];
  } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const { toast } = useToast();

  const handleImageSelected = (file: File | null) => {
    if (file) {
      setSelectedImage(file);
      setAppState(AppState.IMAGE_SELECTED);
    } else {
      setSelectedImage(null);
      setAppState(AppState.INITIAL);
    }
  };

  const handleDetectObjects = async () => {
    if (!selectedImage) return;
    
    try {
      setAppState(AppState.PROCESSING);
      
      // Call the API (mock in this case)
      const result = await mockDetectObjects(selectedImage);
      
      setResults(result);
      setAppState(AppState.RESULTS);
    } catch (err) {
      setError("Failed to process the image. Please try again or use a different image.");
      setAppState(AppState.ERROR);
      toast({
        title: "Error processing image",
        description: "Something went wrong. Please try again.",
        variant: "destructive"
      });
    }
  };

  const handleAnalyzeAnother = () => {
    setSelectedImage(null);
    setResults(null);
    setError(null);
    setAppState(AppState.INITIAL);
  };

  return (
    <div className="min-h-screen bg-background">
      <div className="container py-12 max-w-6xl">
        <Header />
        
        <div className="bg-card rounded-xl shadow-sm p-8 mb-8">
          <h2 className="text-2xl font-medium mb-6">Object Detection</h2>
          
          {appState === AppState.RESULTS && results ? (
            <ResultDisplay 
              imageUrl={results.imageUrl}
              detections={results.detections}
              onAnalyzeAnother={handleAnalyzeAnother}
            />
          ) : (
            <div className="relative">
              <UploadZone 
                onImageSelected={handleImageSelected} 
                selectedImage={selectedImage}
              />
              
              {appState === AppState.PROCESSING && <ProcessingLoader />}
              
              {appState === AppState.IMAGE_SELECTED && selectedImage && (
                <div className="flex justify-center mt-4">
                  <Button
                    className="bg-accent hover:bg-accent/80"
                    onClick={handleDetectObjects}
                  >
                    Detect Objects
                  </Button>
                </div>
              )}
              
              {appState === AppState.ERROR && error && (
                <div className="mt-4 p-4 bg-destructive/10 text-destructive rounded-md">
                  <p>{error}</p>
                  <Button variant="outline" onClick={handleAnalyzeAnother} className="mt-2">
                    Try Again
                  </Button>
                </div>
              )}
            </div>
          )}
        </div>
        
        <div className="text-center text-sm text-muted-foreground">
          <p>Upload an image to detect and analyze objects using AI.</p>
        </div>
      </div>
    </div>
  );
};

export default Index;
