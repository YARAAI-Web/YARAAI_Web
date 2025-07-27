rule auto_rule_20250727022752_6900 {
  strings:
    $o0 = "__getcallerseflags" wide ascii nocase
    $o1 = "x4E54" wide ascii nocase
  condition:
    all of them
}