rule auto_rule_20250726112430_6284 {
  strings:
    $o0 = "x4E50" wide ascii nocase
    $o1 = "x1FC0" wide ascii nocase
    $o2 = "_GetUserObjectSecurityGetUserObjectSecu" wide ascii nocase
  condition:
    3 of ($o*)
}