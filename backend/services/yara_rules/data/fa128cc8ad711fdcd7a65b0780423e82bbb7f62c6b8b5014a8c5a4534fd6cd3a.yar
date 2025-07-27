rule auto_rule_20250727035030_5294 {
  strings:
    $o0 = "hJob" wide ascii nocase
    $o1 = "lpmi" wide ascii nocase
    $o2 = "pcbi" wide ascii nocase
    $o3 = "wNewWord" wide ascii nocase
  condition:
    4 of ($o*)
}