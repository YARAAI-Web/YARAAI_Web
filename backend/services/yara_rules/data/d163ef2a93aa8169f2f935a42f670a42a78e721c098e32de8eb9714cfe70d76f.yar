rule auto_rule_20250726195351_3568 {
  strings:
    $o0 = "CreateMailslotW" wide ascii nocase
    $o1 = "lpte" wide ascii nocase
    $o2 = "CountClipboardFormats" wide ascii nocase
    $o3 = "CreatePropertySheetPageA" wide ascii nocase
    $o4 = "hObj" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726195354_1850 {
  strings:
    $o0 = "GetClipboardOwner" wide ascii nocase
    $o1 = "fIcon" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726195359_9562 {
  condition:
    auto_rule_20250726195351_3568 or auto_rule_20250726195354_1850
}