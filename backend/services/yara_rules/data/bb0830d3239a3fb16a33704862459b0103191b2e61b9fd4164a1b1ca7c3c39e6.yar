rule auto_rule_20250727005002_1830 {
  strings:
    $o0 = "xEE46EAFC" wide ascii nocase
    $o1 = "x481Du" wide ascii nocase
    $o2 = "x8FDC9A8FB91FABF2uLL" wide ascii nocase
    $o3 = "x3B16u" wide ascii nocase
  condition:
    4 of ($o*)
}