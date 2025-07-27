rule auto_rule_20250726145644_9383 {
  strings:
    $o0 = "UnicodeToUtf8" wide ascii nocase
    $o1 = "lpFindFileData" wide ascii nocase
    $o2 = "CompareStringA_0" wide ascii nocase
    $o3 = "byte_489714" wide ascii nocase
    $o4 = "UTF8Decode" wide ascii nocase
  condition:
    4 of ($o*)
}