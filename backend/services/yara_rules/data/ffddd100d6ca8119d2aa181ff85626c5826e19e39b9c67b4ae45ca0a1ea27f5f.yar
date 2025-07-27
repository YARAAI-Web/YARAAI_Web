rule auto_rule_20250726130859_1499 {
  strings:
    $o0 = "cyWidth" wide ascii nocase
    $o1 = "PageSetupDlgA" wide ascii nocase
    $o2 = "GetFileTitleW" wide ascii nocase
    $o3 = "himlSrc" wide ascii nocase
    $o4 = "lpNumberOfEventsRead" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726130902_0085 {
  strings:
    $o0 = "himlDrag" wide ascii nocase
    $o1 = "dxBitmap" wide ascii nocase
    $o2 = "nBitmaps" wide ascii nocase
    $o3 = "yHotSpot" wide ascii nocase
    $o4 = "constPropSheetPagePointer" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726130907_0319 {
  condition:
    auto_rule_20250726130859_1499 or auto_rule_20250726130902_0085
}