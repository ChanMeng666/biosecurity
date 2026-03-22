import { GuideForm } from "@/components/guides/guide-form";

export default function StaffAddGuidePage() {
  return (
    <div className="max-w-3xl">
      <h2 className="text-lg font-semibold mb-6">Add New Guide</h2>
      <GuideForm submitUrl="/api/guides" method="POST" returnUrl="/staff/manage-guides" />
    </div>
  );
}
