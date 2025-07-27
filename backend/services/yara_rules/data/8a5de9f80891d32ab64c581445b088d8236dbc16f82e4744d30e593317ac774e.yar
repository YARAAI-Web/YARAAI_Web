rule auto_rule_20250726182610_8736 {
  strings:
    $o0 = "hTemplateFile" wide ascii nocase
    $o1 = "aGsyst1232Cgcri_0" wide ascii nocase
    $o2 = "dwCreationDisposition" wide ascii nocase
  condition:
    3 of ($o*)
}