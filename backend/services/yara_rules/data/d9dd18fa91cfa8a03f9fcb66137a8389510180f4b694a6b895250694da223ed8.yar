rule auto_rule_20250726195921_0349 {
  strings:
    $o0 = "off_41E02C" wide ascii nocase
    $o1 = "DateStr" wide ascii nocase
    $o2 = "off_41E05C" wide ascii nocase
    $o3 = "yOUVHLM" wide ascii nocase
    $o4 = "dword_40BE10" wide ascii nocase
  condition:
    4 of ($o*)
}