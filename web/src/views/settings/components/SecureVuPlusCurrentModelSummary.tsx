import {
  SettingsGroupCard,
  SplitCardRow,
} from "@/components/card/SettingsGroupCard";
import type { SecureVuConfig } from "@/types/securevuConfig";
import { useTranslation } from "react-i18next";

type SecureVuPlusCurrentModelSummaryProps = {
  plusModel: SecureVuConfig["model"]["plus"];
};

export default function SecureVuPlusCurrentModelSummary({
  plusModel,
}: SecureVuPlusCurrentModelSummaryProps) {
  const { t } = useTranslation("views/settings");

  return (
    <SettingsGroupCard title={t("securevuPlus.cardTitles.currentModel")}>
      {plusModel === undefined && (
        <p className="text-muted-foreground">
          {t("securevuPlus.modelInfo.loading")}
        </p>
      )}
      {plusModel === null && (
        <p className="text-danger">{t("securevuPlus.modelInfo.error")}</p>
      )}
      {plusModel && (
        <div className="space-y-6">
          <SplitCardRow
            label={t("securevuPlus.modelInfo.baseModel")}
            content={
              <p>
                {plusModel.baseModel} (
                {plusModel.isBaseModel
                  ? t("securevuPlus.modelInfo.plusModelType.baseModel")
                  : t("securevuPlus.modelInfo.plusModelType.userModel")}
                )
              </p>
            }
          />
          <SplitCardRow
            label={t("securevuPlus.modelInfo.trainDate")}
            content={<p>{new Date(plusModel.trainDate).toLocaleString()}</p>}
          />
          <SplitCardRow
            label={t("securevuPlus.modelInfo.modelType")}
            content={
              <p>
                {plusModel.name} ({plusModel.width + "x" + plusModel.height})
              </p>
            }
          />
          <SplitCardRow
            label={t("securevuPlus.modelInfo.supportedDetectors")}
            content={<p>{plusModel.supportedDetectors.join(", ")}</p>}
          />
        </div>
      )}
    </SettingsGroupCard>
  );
}
