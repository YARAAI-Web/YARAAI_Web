rule auto_rule_20250726133610_6431 {
  strings:
    $o0 = "dword_420F6C" wide ascii nocase
    $o1 = "x766Du" wide ascii nocase
    $o2 = "dword_420F64" wide ascii nocase
  condition:
    3 of ($o*)
}