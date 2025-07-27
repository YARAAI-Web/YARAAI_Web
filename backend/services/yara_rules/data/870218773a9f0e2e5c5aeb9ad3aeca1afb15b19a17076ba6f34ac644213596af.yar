rule auto_rule_20250727033028_6513 {
  strings:
    $o0 = "__crtGetShowWindowMode" wide ascii nocase
    $o1 = "dword_4C2240" wide ascii nocase
  condition:
    all of them
}