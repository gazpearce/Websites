---
title: "Cat6 vs Cat5e for CCTV and Smart Home: What UK Installers Actually Recommend in 2026"
description: "Expert installer comparison of Cat6 vs Cat5e for CCTV, smart home, and PoE in UK homes. Pure copper vs CCA, Part R compliance, 4K bandwidth needs, and real installation advice from Newcastle to Middlesbrough."
date: 2026-06-24T08:00:00+01:00
draft: false
tags:
  - "Cat6"
  - "Cat5e"
  - "CCTV cabling"
  - "PoE"
  - "data cabling"
  - "smart home cabling"
  - "UK installer"
categories:
  - "Data Cabling"
  - "CCTV Installation"
series: "CCTV Cabling Guide 2026"
author: "Gary Pearce"
showToc: true
weight: 1
---

![Ethernet cable being terminated for CCTV installation](https://files.catbox.moe/uv5prv.webp)

## Quick Answer

**Use Cat6 pure copper for any new CCTV or smart home installation in 2026.** Cat5e still works for basic 1080p cameras on short runs, but the cable cost difference is negligible (£10–£20 per 100m) while the labour to install it is identical. Cat6 handles 4K cameras, PoE+ heat, and future upgrades without rewiring. The only exception: if you're working with existing Cat5e that's already installed and working, leave it alone.

---

## Key Takeaways

| Factor | Cat5e | Cat6 |
|---|---|---|
| Max speed | 1 Gbps at 100m | 10 Gbps at 55m, 1 Gbps at 100m |
| 4K CCTV support | OK for 1–2 cameras | Recommended for 4+ cameras |
| PoE+ (30W) handling | Marginal over 25m | Comfortable to 100m |
| CCA risk | Very common in cheap cable | Less common but still present |
| Labour cost to install | Identical | Identical |
| Cable cost per 100m | £25–£40 | £35–£60 |
| Part R compliance | Meets minimum | Exceeds minimum |
| Future-proof to 2030+ | No | Yes |

---

![Ethernet cable categories comparison — Cat5e, Cat6, Cat6a side by side](https://files.catbox.moe/s7z9by.webp)

## Introduction

I've installed data cabling for CCTV and smart home systems across Newcastle, Durham, Sunderland, Middlesbrough, and thirty other UK towns for over a decade. The single question I get asked most often hasn't changed in five years: "Should I use Cat5e or Cat6?"

Most online guides answer this with a spec sheet. Cat5e does 1 Gbps. Cat6 does 10 Gbps at shorter distances. Job done, right? Not even close. The real answer depends on cable length, camera resolution, PoE power draw, whether you're dealing with CCA (copper-clad aluminium) versus pure copper, and — most importantly — what your property will need in five years.

This guide comes from pulling thousands of metres of cable through lofts, cavity walls, conduits, and trenches across the North East. It's not theoretical. It's what I actually use, what I avoid, and why.

---

## The Real Difference Between Cat5e and Cat6

On paper, the specs are straightforward. In practice, three differences matter more than the raw numbers.

### 1. Conductor Thickness

Cat5e typically uses 24 AWG conductors. Cat6 uses 23 AWG. That one gauge difference means Cat6 has roughly 20% more copper cross-section. For PoE — where power travels alongside data — that extra copper reduces voltage drop and heat buildup over longer runs. A Cat5e run at 45 metres carrying a 30W PoE+ camera will run noticeably warmer than the same run in Cat6.

### 2. Internal Spline

Cat6 cable has a plastic central cross — the spline — that physically separates the four twisted pairs. This reduces crosstalk (signal bleeding between pairs) and maintains signal integrity at higher frequencies. Cat5e has no spline. The spline also makes Cat6 stiffer, which matters when routing through tight spaces.

### 3. Bandwidth Headroom

Cat5e is rated for 100 MHz. Cat6 is rated for 250 MHz. For a single 1080p camera streaming at 5–10 Mbps, neither cable breaks a sweat. But modern 4K cameras can push 30–50 Mbps each, and an 8-camera NVR recording continuously needs to move 240–400 Mbps. On Cat5e, that's 24–40% of the cable's theoretical capacity. On Cat6, it's 24–40% of a much higher ceiling. Headroom matters when your NVR is also handling remote viewing, motion alerts, and AI analytics.

---

![CCA vs pure copper cable cross-section comparison](https://files.catbox.moe/guc08c.webp)

## The CCA Trap — Why Cheap Cable Kills CCTV Systems

CCA — copper-clad aluminium — is the single biggest cause of CCTV cabling failures I see. The cable looks like copper on the outside, but the conductor is aluminium with a thin copper coating. It's cheaper to manufacture and retailers love it because it sells for 30–50% less than pure copper.

Here's the problem: aluminium has roughly 60% higher electrical resistance than copper. For PoE cameras drawing 15–30W, that resistance causes voltage drop and heat buildup. I've seen CCA cables running at 60°C+ on 30-metre PoE+ runs. That heat degrades the cable jacket, increases resistance further, and eventually causes intermittent camera dropouts — usually at night when the IR LEDs kick in and draw maximum power.

**How to spot CCA:**

- The cable is noticeably lighter than pure copper
- Scrape the conductor with a knife — if you see silver/white underneath, it's CCA
- The packaging doesn't say "100% pure copper" or "solid bare copper"
- It's suspiciously cheap (under £30 for 100m of Cat6)

I refuse to install CCA cable on any job. It voids equipment warranties, fails prematurely, and the labour cost to replace it is always more than the saving upfront. Use solid bare copper Cat6 — Excel, Dintek, or branded cable from a proper distributor, not Amazon Marketplace.

---

## PoE and Heat — Why Cat6 Handles Power Better on Long Runs

Power over Ethernet has changed CCTV installation completely. One cable carries data and power up to 100 metres. But PoE isn't free — every watt travelling down a copper cable generates heat, and the thinner the conductor, the more heat.

| PoE Standard | Power Delivered | Typical Use |
|---|---|---|
| PoE (802.3af) | 15.4W | Basic IP cameras |
| PoE+ (802.3at) | 30W | PTZ cameras, IR illuminators |
| PoE++ (802.3bt) | 60–90W | High-power PTZ, heater/blowers |

For a standard 4K PoE+ camera at 25 metres, the difference in heat generation between Cat5e and Cat6 is minimal. At 50 metres, Cat6 runs about 5°C cooler. At 75 metres, that gap widens to 10–12°C. On a camera with IR LEDs running all night, that's the difference between a stable connection and random dropouts at 3am.

I tested this on a job in Gateshead last year. A customer had intermittent camera failures on three Hikvision ColorVu cameras running over 60 metres of Cat5e CCA (installed by another company). The cameras worked perfectly during the day but dropped offline at night. Re-terminating onto pure copper Cat6 eliminated every dropout. The issue wasn't the camera — it was the cable.

---

## Cat5e vs Cat6 for 4K CCTV Cameras — Real Bandwidth Needs

Here's the bandwidth math most installers don't tell you:

- 1080p camera at 15fps: ~5 Mbps
- 4K camera at 20fps: ~25 Mbps  
- 4K camera at 30fps: ~40 Mbps
- 4K camera with H.265+ compression: ~15–20 Mbps

An 8-camera 4K system on H.265+ generates roughly 120–160 Mbps continuous. Cat5e handles that comfortably on paper. The problem is that most domestic routers and NVRs don't maintain full gigabit throughput on all ports simultaneously, and Cat5e leaves zero headroom for burst traffic, firmware updates, or remote viewing.

I recommend Cat6 for any system with more than two 4K cameras, or any system where the NVR is more than 20 metres from the router. For a standard 4-camera home system with 1080p or 2K cameras on short runs, Cat5e works fine — but only if it's pure copper, properly terminated, and tested.

---

![Cat6 vs Cat5e decision guide infographic for UK CCTV installers](https://files.catbox.moe/erftxi.png)

## What About Cat6a, Cat7, and Cat8?

**Cat6a:** Supports 10 Gbps at the full 100 metres. Heavier, stiffer, and about 40% more expensive than Cat6. Worth it for backbone runs between network cabinets, or for commercial installations where you expect 10 Gbps in the next 5–10 years. Overkill for domestic CCTV.

**Cat7:** Not a recognised IEEE standard in the UK. Proprietary GG45 connectors are hard to source and terminate. I don't use it and I don't recommend it.

**Cat8:** 25–40 Gbps at 30 metres. Data centre cable. Completely unnecessary for any CCTV or smart home system in 2026.

For UK homes and small businesses, Cat6 is the sweet spot. It handles everything current cameras need, supports PoE++ without issue, and will still be adequate when 8K cameras arrive in 3–5 years.

---

## UK Building Regulations and Part R Compliance

Since 2022, Part R of UK Building Regulations requires all new dwellings to have a network termination point and internal cabling suitable for gigabit-capable broadband. In practice, Building Control officers increasingly ask for evidence that new homes are "gigabit-ready."

Cat5e meets the minimum requirement. But if you're building or renovating, install Cat6. The cost difference is tiny compared to the overall build budget, and it ensures compliance with any future tightening of the regulations. I wrote about this in more detail in my guide to <a href="/posts/cctv-for-new-build-homes-2026/">pre-wiring for new build homes</a>.

For existing homes, Part R doesn't apply retroactively. But if you're running new cable anyway, the same logic applies — Cat6 now means no re-cable later.

---

## When I Actually Use Cat5e (and Why)

Despite everything above, I do still use Cat5e in specific situations:

1. **Very short runs under 10 metres** — For a single camera on a short drop to a PoE switch, Cat5e pure copper is fine. The heat and bandwidth differences are negligible.

2. **Retrofit in tight spaces** — Cat5e is thinner and more flexible. When I'm threading cable through a 10mm gap behind existing coving or into a shallow conduit, Cat5e goes where Cat6 won't.

3. **Temporary installations** — For rental properties or short-term setups where the cable will be removed in 12–24 months, Cat5e keeps costs down.

4. **Customer on a strict budget** — If a customer genuinely can't afford the £20–£30 premium for Cat6 across a whole system, I'll run Cat5e pure copper with a note that it's a compromise. I won't install CCA under any circumstances.

These are edge cases. For 90% of installations, Cat6 is the right choice.

---

## Cable Installation Tips from Real Jobs

### Do Not Run Ethernet Parallel to Mains Cable

BS 7671 recommends a minimum 100mm separation between Band I (data) and Band II (mains) cables running in parallel. I've fixed countless systems where interference from mains cables caused video glitching or intermittent PoE dropouts. If you can't maintain separation, use shielded Cat6 (STP) and earth it properly at the patch panel end.

### Test Every Run

I use a Fluke Networks cable tester on every single run. Wire map, length, and continuity checks catch terminations that look fine but will fail at 3am under PoE load. A basic continuity tester is £30 and will save you a return visit.

### Label Both Ends

Every cable gets a unique number written on heat-shrink labels at both ends, matching a cable schedule. I've been called to jobs where 20 unlabelled cables disappear into a ceiling void and nobody knows which one goes where. Labelling takes five minutes per cable and saves hours of fault-finding.

### Use a Patch Panel

Terminating cables directly into an NVR or switch with RJ45 plugs is common but not best practice. A patch panel at the cabinet end gives you a solid punch-down termination point, and short patch leads connect to the switch. If a port fails, you replace a £2 patch lead instead of re-terminating a cable run. See my <a href="/posts/structured-cabling-cctv-uk-2026/">structured cabling guide</a> for the full setup.

### Leave Service Loops

Leave 1–2 metres of spare cable coiled at both ends. Cameras move, cabinets get reorganised, and having slack cable means you can re-terminate without pulling new runs.

---

## Comparison Table

### Cat5e vs Cat6 vs Cat6a — Which to Use

| Cable Type | Max Speed | Max Distance for 10 Gbps | PoE+ Suitability | Flexibility | Price per 100m | Best For |
|---|---|---|---|---|---|---|
| Cat5e | 1 Gbps | N/A | Marginal over 25m | High | £25–£40 | Short runs, budget installs, temporary setups |
| Cat6 | 1 Gbps/10 Gbps | 55m | Yes to 100m | Medium | £35–£60 | **Most installations — recommended default** |
| Cat6a | 10 Gbps | 100m | Yes to 100m | Low | £55–£90 | Commercial backbone, long runs, high-interference areas |
| Cat7 | 10 Gbps | 100m | Yes | Low | £70–£120 | Not recommended for CCTV |
| Cat8 | 25–40 Gbps | 30m | Yes | Very low | £100+ | Data centres only |

---

{{< youtube uZCfo7TeVvs >}}

## Frequently Asked Questions

### Can I run Cat6 and Cat5e on the same CCTV system?

Yes, they're fully compatible. Both use the same RJ45 connectors and follow the same T568A or T568B wiring standard. The network will run at the speed of the slowest segment, so mixing them doesn't cause problems — but consistency makes fault-finding easier. Read our <a href="/posts/cat5e-vs-cat6-vs-cat6a-which-cable-do-you-actually-need-2026/">full cable category comparison</a> for more detail.

### Is Cat5e good enough for 4K CCTV cameras?

For a single 4K camera on a short run (under 20 metres), Cat5e pure copper will work. For multiple 4K cameras, or runs over 20 metres, use Cat6. The bandwidth headroom matters more than many installers admit, especially when IR illuminators draw peak power at night. Our <a href="/posts/best-cctv-cameras-uk-homes-2026/">CCTV camera guide</a> covers which cameras need what cable.

### How do I know if my ethernet cable is CCA?

Scrape the conductor with a knife. If the core is silver or white underneath the copper coating, it's CCA. Pure copper is copper all the way through. Also check the packaging — it must say "100% solid bare copper" or equivalent. If it doesn't say, assume it's CCA. See our <a href="/posts/cca-vs-pure-copper-ethernet-uk-2026/">CCA vs pure copper guide</a> for photos and test methods.

### Does Cat6 improve PoE performance for outdoor cameras?

Yes. Cat6's thicker 23 AWG conductors carry PoE+ more efficiently over longer distances, with less voltage drop and heat generation. For outdoor cameras where cable runs often exceed 20 metres — from the cabinet to the eaves, then across the soffit — Cat6 maintains stable power delivery. Our <a href="/posts/outdoor-poe-camera-cabling-uk-2026/">outdoor PoE cabling guide</a> covers weatherproofing and surge protection.

### What cable should I use for smart home devices like video doorbells and access points?

Cat6 to every location. Video doorbells, smart speakers, WiFi access points, and smart home hubs all benefit from wired backhaul. A single Cat6 run to a ceiling position in the hallway lets you mount a PoE access point that covers the whole ground floor. For smart home cabling strategy, see <a href="/posts/smart-home-pre-wiring-checklist-uk-2026/">our pre-wiring checklist</a>.

### Do I need shielded Cat6 for CCTV?

Only when the cable runs parallel to mains electrical cables within 100mm, or in commercial environments with heavy machinery, fluorescent lighting, or variable speed drives. For a standard UK home installation, unshielded Cat6 (U/UTP) is fine. Shielded cable must be properly earthed at the patch panel — if it isn't, shielding can actually make interference worse.

### Can I use existing telephone cable for CCTV?

No. Telephone cable (Cat3 or CW1308) cannot support PoE and lacks the bandwidth for video. It's not rated for the current or frequency that IP cameras need. Run new Cat6.

---

## Expert Recommendations

| Situation | Cable Choice | Why |
|---|---|---|
| 1080p camera, run under 15m | Cat5e pure copper | Fine for low bandwidth, short distance |
| 4K camera, any distance | Cat6 pure copper | Bandwidth headroom and PoE stability |
| 8+ camera system | Cat6 pure copper | Aggregate bandwidth needs Cat6 |
| New build pre-wire | Cat6 pure copper | Part R compliance and future-proofing |
| Commercial installation | Cat6a for backbone, Cat6 for drops | 10 Gbps backbone for future upgrades |
| Outdoor camera run over 30m | Cat6 pure copper STP | Better noise rejection and PoE delivery |
| Retrofit in tight void | Cat5e pure copper (if necessary) | Flexibility advantage, but only if Cat6 won't fit |

---

## Common Mistakes

**CCA cable.** The most expensive "saving" you'll make. Cheap cable causes intermittent faults that are a nightmare to diagnose. Pay for pure copper.

**Cable too close to mains.** 100mm minimum separation. Closer than that and you get interference that manifests as video glitching, packet loss, or failed PoE negotiation. Use shielded cable if separation is impossible.

**No test after termination.** A cable that passes continuity at installation can fail under PoE load at 3am. Test every run with a proper cable tester. Basic testers cost £30 and will save you return visits.

**Running cable without a plan.** I've seen cameras daisy-chained, cables stapled through insulation, and runs exceeding 100 metres with no repeater. Plan your routes before pulling cable. Measure twice, cut once.

**Using pre-terminated patch leads for permanent installation.** Pre-made patch leads use stranded conductors that have higher resistance than solid cable. They're fine for short patch connections between switch and patch panel, but not for in-wall runs. Use solid-core cable for infrastructure, stranded patch leads for connections.

---

## Conclusion

The default answer for any new CCTV or smart home installation in 2026 is **Cat6 pure copper**. It costs negligibly more than Cat5e, installs in the same time, and saves your customer from a re-cable when they upgrade to 4K or 8K cameras. Cat5e still has a place — short runs, tight spaces, budget constraints — but it's the exception, not the rule.

If you're installing in the North East, Yorkshire, or the North West and need a survey or installation, <a href="tel:[Contact Form Online]">get in touch</a>. I'll quote Cat6 as standard unless there's a specific reason not to.

For related reading, check out our guides on <a href="/posts/best-cctv-cameras-uk-homes-2026/">choosing CCTV cameras</a>, <a href="/posts/wireless-alarm-systems-uk-homes-2026/">wireless alarm systems</a>, and <a href="/posts/cctv-for-offices-commercial-buildings-uk-2026/">commercial CCTV installations</a>.

---

*About the author: Gary Pearce is an NSI and SSAIB certified security systems installer working across Newcastle, Durham, Sunderland, Middlesbrough, Manchester, Leeds, and the wider North. He has installed data cabling and CCTV systems in over 1,000 properties. Contact: [Contact Form Online] | info@hardwire.uk*

