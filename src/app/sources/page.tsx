import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ExternalLink } from "lucide-react";

const sources = [
  {
    title: "Ministry for Primary Industries (MPI)",
    description: "New Zealand government agency responsible for biosecurity.",
    url: "https://www.mpi.govt.nz",
  },
  {
    title: "Department of Agriculture, Water and the Environment",
    description: "Australian government department managing biosecurity.",
    url: "https://www.agriculture.gov.au",
  },
  {
    title: "CABI - Invasive Species Compendium",
    description: "Comprehensive reference for invasive species worldwide.",
    url: "https://www.cabi.org/isc",
  },
  {
    title: "Global Invasive Species Database (GISD)",
    description: "Database of invasive species maintained by the IUCN.",
    url: "http://www.iucngisd.org/gisd",
  },
  {
    title: "Pixabay",
    description: "Source for royalty-free images used in the guide library.",
    url: "https://pixabay.com",
  },
];

export default function SourcesPage() {
  return (
    <div className="flex-1 bg-gray-50">
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-3xl mx-auto">
          <h1 className="text-3xl font-bold mb-2">Sources & Credits</h1>
          <p className="text-muted-foreground mb-8">
            Information and resources used in the Biosecurity Guide platform.
          </p>

          <div className="space-y-4">
            {sources.map((source) => (
              <Card key={source.title}>
                <CardHeader className="pb-2">
                  <CardTitle className="text-base flex items-center gap-2">
                    {source.title}
                    <a
                      href={source.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-emerald-600 hover:text-emerald-700"
                    >
                      <ExternalLink className="h-4 w-4" />
                    </a>
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground">{source.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
