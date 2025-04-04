
import { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, X } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';
import { useToast } from '@/hooks/use-toast';

interface UploadZoneProps {
  onImageSelected: (file: File) => void;
  selectedImage: File | null;
}

const UploadZone = ({ onImageSelected, selectedImage }: UploadZoneProps) => {
  const [preview, setPreview] = useState<string | null>(null);
  const { toast } = useToast();

  const onDrop = useCallback(
    (acceptedFiles: File[]) => {
      if (acceptedFiles.length === 0) return;
      
      const file = acceptedFiles[0];
      
      // Check file type and size
      if (!file.type.match('image.*')) {
        toast({
          title: "Invalid file type",
          description: "Please upload an image file (JPG, PNG, WEBP)",
          variant: "destructive"
        });
        return;
      }
      
      if (file.size > 10 * 1024 * 1024) { // 10MB limit
        toast({
          title: "File too large",
          description: "Image must be less than 10MB",
          variant: "destructive"
        });
        return;
      }
      
      // Create preview
      const reader = new FileReader();
      reader.onload = () => {
        setPreview(reader.result as string);
      };
      reader.readAsDataURL(file);
      
      onImageSelected(file);
    },
    [onImageSelected, toast]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ 
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.webp']
    },
    maxFiles: 1
  });

  const handleClearImage = () => {
    setPreview(null);
    onImageSelected(null as unknown as File);
  };

  return (
    <div className={cn(
      "upload-zone",
      isDragActive && "upload-zone-active",
      selectedImage && "border-solid border-accent/50"
    )} {...getRootProps()}>
      <input {...getInputProps()} />
      
      {!selectedImage ? (
        <>
          <Upload className="w-16 h-16 text-accent mb-4" />
          <p className="text-lg font-medium">Drag & Drop Your Image Here</p>
          <p className="text-sm text-muted-foreground mt-2">or Click to Browse Files</p>
          <Button className="mt-4 bg-accent hover:bg-accent/80">Select Image</Button>
          <p className="text-xs text-muted-foreground mt-4">
            Supports: JPG, PNG, WEBP (Max: 10MB)
          </p>
        </>
      ) : (
        <div className="relative w-full h-full flex items-center justify-center">
          {preview && (
            <>
              <img 
                src={preview} 
                alt="Preview" 
                className="max-h-64 max-w-full object-contain rounded-md"
              />
              <button 
                onClick={(e) => {
                  e.stopPropagation();
                  handleClearImage();
                }}
                className="absolute top-2 right-2 bg-background/80 p-1 rounded-full hover:bg-background"
              >
                <X className="w-5 h-5" />
              </button>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default UploadZone;
