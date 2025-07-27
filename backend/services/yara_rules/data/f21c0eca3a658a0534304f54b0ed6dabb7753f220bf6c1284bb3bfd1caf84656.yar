rule auto_rule_20250727012156_1449 {
  strings:
    $o0 = "unknown_libname_69" wide ascii nocase
    $o1 = "byte_4735BC" wide ascii nocase
    $o2 = "Delphi6" wide ascii nocase
  condition:
    3 of ($o*)
}