rule auto_rule_20250726082910_4634 {
  strings:
    $o0 = "__crtGetEnvironmentStringsA" wide ascii nocase
    $o1 = "dword_45CDC0" wide ascii nocase
    $o2 = "_msize" wide ascii nocase
  condition:
    3 of ($o*)
}