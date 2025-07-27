rule auto_rule_20250726210359_3314 {
  strings:
    $o0 = "DefDlgProcA" wide ascii nocase
    $o1 = "lpProgressRoutine" wide ascii nocase
    $o2 = "UnregisterClassW" wide ascii nocase
    $o3 = "IsValidLocale" wide ascii nocase
    $o4 = "lReadTimeout" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726210402_2262 {
  strings:
    $o0 = "lpThreadAttributes" wide ascii nocase
    $o1 = "WriteFileEx" wide ascii nocase
    $o2 = "hTemplateFile" wide ascii nocase
    $o3 = "lprc" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726210406_9086 {
  condition:
    auto_rule_20250726210359_3314 or auto_rule_20250726210402_2262
}