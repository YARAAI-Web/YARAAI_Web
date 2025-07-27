rule auto_rule_20250726070745_0626 {
  strings:
    $o0 = "EECh" wide ascii nocase
    $o1 = "byte_6402E068" wide ascii nocase
    $o2 = "ntohl" wide ascii nocase
  condition:
    3 of ($o*)
}