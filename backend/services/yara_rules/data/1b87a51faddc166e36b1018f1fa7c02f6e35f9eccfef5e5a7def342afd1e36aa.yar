rule auto_rule_20250726195727_5136 {
  strings:
    $o0 = "SetFileApisToOEM" wide ascii nocase
    $o1 = "IMPQueryIMEA" wide ascii nocase
    $o2 = "lpBaseAddress" wide ascii nocase
  condition:
    3 of ($o*)
}