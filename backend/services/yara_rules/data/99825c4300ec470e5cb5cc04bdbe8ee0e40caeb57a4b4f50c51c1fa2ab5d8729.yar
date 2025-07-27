rule auto_rule_20250727020553_9747 {
  strings:
    $o0 = "start_6" wide ascii nocase
    $o1 = "__crtGetShowWindowMode" wide ascii nocase
    $o2 = "fprem1" wide ascii nocase
  condition:
    3 of ($o*)
}