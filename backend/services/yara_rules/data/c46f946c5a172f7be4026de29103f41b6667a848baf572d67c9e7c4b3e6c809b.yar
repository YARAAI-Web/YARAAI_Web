rule auto_rule_20250726083307_4719 {
  strings:
    $o0 = "DialogBoxIndirectParamW" wide ascii nocase
    $o1 = "gaFlags" wide ascii nocase
    $o2 = "RegisterClassExA" wide ascii nocase
    $o3 = "GetWindowDC" wide ascii nocase
    $o4 = "byte_41DA2C" wide ascii nocase
  condition:
    4 of ($o*)
}